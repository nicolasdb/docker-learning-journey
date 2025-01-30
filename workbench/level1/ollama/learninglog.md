simple enough: 

from docker hub:

```bash
docker pull ollama/ollama

docker run -d --restart unless-stopped -v ollama:/root/.ollama -p 11434:11434 --name ollama-cpu ollama/ollama
```

And I choosed qwen2.5, a lightweight model.
Then to run a command from inside the container:
`docker exec -it ollama ollama run qwen2.5:1.5b`

> **note:** I'm only able to run CPU version on my laptop, GPU Nvidia is too old and linux driver doesn't install on pop.OS 22.04, don't understand why.
But hey, it's slow but it works!
