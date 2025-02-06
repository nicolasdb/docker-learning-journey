import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from supabase import create_client
import os
from datetime import datetime

# Initialize Supabase client
supabase = create_client(
    os.getenv("SUPABASE_URL", ""),
    os.getenv("SUPABASE_KEY", "")
)

def load_questions():
    """Load questions from either CSV or Supabase based on configuration"""
    questions_source = os.getenv("QUESTIONS_SOURCE", "csv")
    
    if questions_source == "supabase":
        table_name = os.getenv("QUESTIONS_TABLE", "maturity_questions")
        context_id = os.getenv("CONTEXT_ID")
        response = supabase.table(table_name)\
            .select("*")\
            .eq("context_id", context_id)\
            .execute()
        return pd.DataFrame(response.data)
    else:
        questions_file = os.getenv("QUESTIONS_FILE", "/data/questions.csv")
        return pd.read_csv(questions_file)

# Define scoring system with exponential progression
OPTION_SCORES = [0, 1, 2, 4, 8]  # Exponential progression (powers of 2)

def calculate_scores(responses, questions_df):
    """Calculate detailed scores for each section"""
    results = {}
    
    for section in questions_df['section'].unique():
        section_questions = questions_df[questions_df['section'] == section]
        section_data = {
            'questions': {},
            'raw_score': 0,
            'max_possible': len(section_questions) * OPTION_SCORES[-1],
            'percentage': 0
        }
        
        # Calculate scores for each question in the section
        for idx in section_questions.index:
            response_idx = responses.get(str(idx), 0)
            question_score = OPTION_SCORES[response_idx]
            question_data = {
                'question': section_questions.loc[idx, 'question'],
                'selected_option': section_questions.loc[idx, f'option{response_idx + 1}'],
                'score': question_score,
                'max_score': OPTION_SCORES[-1]
            }
            section_data['questions'][str(idx)] = question_data
            section_data['raw_score'] += question_score
        
        # Calculate percentage (for backend use only)
        if section_data['max_possible'] > 0:
            section_data['percentage'] = (section_data['raw_score'] / section_data['max_possible']) * 100
        
        results[section] = section_data
    
    # Calculate total scores
    total_raw = sum(section['raw_score'] for section in results.values())
    total_max = sum(section['max_possible'] for section in results.values())
    total_percentage = (total_raw / total_max * 100) if total_max > 0 else 0
    
    return {
        'sections': results,
        'total_raw': total_raw,
        'total_max': total_max,
        'total_percentage': total_percentage
    }

def plot_section_scores(scores):
    """Create a radar chart of section scores"""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='polar')
    
    # Prepare the data
    sections = list(scores['sections'].keys())
    raw_scores = [scores['sections'][section]['raw_score'] for section in sections]
    max_scores = [scores['sections'][section]['max_possible'] for section in sections]
    max_value = max(max_scores)
    
    # Number of variables
    num_vars = len(sections)
    
    # Compute angle for each axis
    angles = [n / float(num_vars) * 2 * np.pi for n in range(num_vars)]
    angles += angles[:1]  # Complete the circle
    
    # Add the scores to complete the circle
    raw_scores += raw_scores[:1]
    
    # Plot data
    ax.plot(angles, raw_scores, 'o-', linewidth=2)
    ax.fill(angles, raw_scores, alpha=0.25)
    
    # Fix axis to go in the right order and start at 12 o'clock
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Set chart limits and grid
    ax.set_ylim(0, max_value)
    grid_ticks = [i * max_value/5 for i in range(6)]  # 5 intervals
    ax.set_rgrids(grid_ticks, angle=0, fontsize=8)
    
    # Draw axis lines for each angle and label
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(sections, fontsize=9)
    
    # Rotate the axis labels to be more readable
    for label, angle in zip(ax.get_xticklabels(), angles[:-1]):
        if angle in (0, np.pi):
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')
    
    # Set chart title
    plt.title("Section Scores", pad=20)
    
    # Add score labels with better positioning
    for angle, section, score, max_score in zip(angles[:-1], sections, raw_scores[:-1], max_scores):
        # Position label based on relative score
        relative_pos = (score / max_value * max_value)
        label_distance = relative_pos + (2 if relative_pos < max_value * 0.8 else -2)
        ha = 'left' if 0 <= angle <= np.pi else 'right'
        label = f'{score}/{max_score}'
        ax.text(angle, label_distance, label,
                ha=ha, va='center', fontsize=9)
    
    plt.tight_layout()
    return fig

def load_previous_results(email):
    """Load previous results for the given email"""
    context_id = os.getenv("CONTEXT_ID")
    response = supabase.table("results")\
        .select("*")\
        .eq("context_id", context_id)\
        .eq("email", email)\
        .order("created_at", desc=True)\
        .limit(1)\
        .execute()
    
    return response.data[0] if response.data else None

def main():
    st.title("Evaluation System")
    
    # Load questions
    questions_df = load_questions()
    
    # Initialize session state for responses if not exists
    if 'responses' not in st.session_state:
        st.session_state.responses = {}
    
    # Create form for questions
    responses = {}
    current_section = None
    
    # Questions section
    st.write("### Evaluation Questions")
    for idx, row in questions_df.iterrows():
        if current_section != row['section']:
            current_section = row['section']
            st.subheader(current_section)
        
        options = [row['option1'], row['option2'], row['option3'], row['option4'], row['option5']]
        response = st.radio(
            row['question'],
            options=options,
            key=f"q_{idx}",
            horizontal=True
        )
        responses[str(idx)] = options.index(response)
        st.session_state.responses = responses
    
    # Calculate and display real-time scores
    if responses:
        scores = calculate_scores(responses, questions_df)
        
        st.write("### Current Scores")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.metric(
                "Total Score", 
                f"{scores['total_raw']}/{scores['total_max']}"
            )
        
        # Plot radar chart
        with col2:
            fig = plot_section_scores(scores)
            st.pyplot(fig)
    
    # Submission section at the bottom
    st.write("---")
    st.write("### Submit Your Evaluation")
    
    # Email and submission form
    with st.form("submission_form"):
        email = st.text_input("Email address")
        
        # Show previous results if available
        if email:
            previous_results = load_previous_results(email)
            if previous_results:
                st.info("Previous submission found")
                with st.expander("View Previous Results"):
                    st.write("### Previous Results")
                    st.write(f"Submitted: {previous_results['created_at']}")
                    st.write(f"Total Score: {previous_results['total_score']}/{previous_results['total_max']}")
                    
                    st.write("#### Section Scores:")
                    section_scores = previous_results['section_scores']
                    for section, data in section_scores.items():
                        st.write(f"**{section}:** {data['raw_score']}/{data['max_possible']}")
                        
                        if st.checkbox(f"Show {section} details"):
                            for q_id, q_data in data['questions'].items():
                                st.write(f"- {q_data['question']}")
                                st.write(f"  Selected: {q_data['selected_option']}")
                                st.write(f"  Points: {q_data['score']}/{q_data['max_score']}")
        
        col1, col2 = st.columns(2)
        with col1:
            save_results = st.checkbox("Save my results", value=True)
        with col2:
            subscribe_mailing = st.checkbox("Subscribe to mailing list")
        
        submitted = st.form_submit_button("Submit Evaluation")
        
        if submitted and email:
            # Calculate final scores
            scores = calculate_scores(responses, questions_df)
            
            # Display results
            st.success("Evaluation completed!")
            st.write(f"Total Score: {scores['total_raw']}/{scores['total_max']}")
            
            # Plot section scores
            fig = plot_section_scores(scores)
            st.pyplot(fig)
            
            if save_results:
                # Save results to Supabase with proper structure
                context_id = os.getenv("CONTEXT_ID")
                result_data = {
                    "context_id": context_id,
                    "email": email,
                    "responses": responses,
                    "section_scores": {
                        section: {
                            "raw_score": data["raw_score"],
                            "max_possible": data["max_possible"],
                            "questions": data["questions"]
                        }
                        for section, data in scores["sections"].items()
                    },
                    "total_score": scores["total_raw"],
                    "total_max": scores["total_max"]
                }
                supabase.table("results").insert(result_data).execute()
            
            if subscribe_mailing:
                try:
                    # Check if already subscribed
                    context_id = os.getenv("CONTEXT_ID")
                    existing = supabase.table("mailing_list")\
                        .select("*")\
                        .eq("email", email)\
                        .eq("context_id", context_id)\
                        .execute()
                    
                    if existing.data:
                        st.info("You're already subscribed to the mailing list!")
                    else:
                        # Add to mailing list
                        mailing_data = {
                            "email": email,
                            "context_id": context_id,
                        }
                        supabase.table("mailing_list").insert(mailing_data).execute()
                        st.success("Successfully subscribed to the mailing list!")
                except Exception as e:
                    st.error(f"Error managing mailing list subscription: {str(e)}")
        
        elif submitted:
            st.error("Please enter your email address")

if __name__ == "__main__":
    main()
