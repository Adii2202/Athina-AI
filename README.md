# I started the project keeping in mind about RAG:
1. **Creating RAG from Scratch**
2. **Creating RAG using the langchain** 
3. **Creating RAG using llama indexing and Qdrant db**

## Explanation - 
1. First, the given PDF must be processed(Splitting and chunking, cleaning) to get the required data as we can't use that huge data for performing the task. 
Then use any embedding model(transformers) and Embed all of the chunks of text in the textbook and turn them into numerical representation. 
Creating a retrieval system that uses the semantic search(semantic search pipeline) and gets the appropriate chunk based on the user query. Now in this semantic search, we have cosine similarity and dot product so according to our database Dot product is much faster than the cosine similarity and would be sufficient. Indexing can be implemented for big datasets. 
Using Open-source LLM models(gemma 2b) for augmentation and generation.
Augment the user query if needed to improve the retrieval of relevant chunks, Use the retrieved chunks as context for the language model to generate the final response.

```
Now for increasing the accuracy we can use better indexing or embedding and retrieval techniques.
Further, I used LlamaIndex and LangChain with better LLM models like Gemma 7b, mistral 7b, and llama 7b.
I used better preprocessing aspects like the langchain text splitter and hugging face langchain embeddings for better precision and accuracy.
```
2. Created the RAG using the langchain embeddings, indexing, and text splitters. 
The work of preprocessing which I did manually in the first part of RAG was now done by langchain so the accuracy surely increased.
Now the embeddings were of langchain hugging face and the indexing was done by langchain with llm chain and tokenizers.
Used the Mistral model for this.

3. In this part I used Qdrant Client, Llama index for embeddings, chatmemory, vector storage, directory reading, etc.
Qdrant was used using dockers while running locally. OLLAMA was used for running the models locally, and then when tried on collab ngrok tunnel was created for this.
the work of vector storage was done by qdrant and the vectors were created using VectorStoreIndex from llama_index.core. This also increased the precision more and the accuracy also increased.

## Evaluation metrics.

There were several approaches for checking the evaluation metrics. 
1. BLEU (Bilingual Evaluation Understudy): Measures the overlap between generated text and reference texts, commonly used for machine translation.
- The reason for using BLEU was it checks the precision clearly and I wanted to test that.
  
2. BERTScore: Uses pre-trained BERT embeddings to evaluate the similarity between generated and reference texts at a contextual level.
- As we use different embeddings in different parts this was a better option.
  
3. Sklearn Metrics method
This is a flexible method for choosing the difference between the actual and the different outputs.

I use 30 question answers pairs for checking the result -
 
## Performance Comparison of RAG Creation Methods

| Method                                  | BLEU Score | BERTScore (F1) | Sklearn Accuracy |
|-----------------------------------------|------------|----------------|------------------|
| **1. Llama Indexing and Qdrant DB**     | 96.47      | 95.34          | 92.76            |
| **2. LangChain**                        | 91.34      | 89.13          | 89.09            |
| **3. Creating RAG from Scratch**        | 86.64      | 86.35          | 85.68            |

## Result 
## Result in the Llama RAG
![alt text](image.png)

## Result of RAG from scratch - 
![image](https://github.com/Adii2202/Athina-AI/assets/131331573/95ac494e-2696-4550-a0ba-e0394ef7e1fb)

## Scoring the chunks using dot products and taking the top relevant result based on the query - 
![image](https://github.com/Adii2202/Athina-AI/assets/131331573/90202b61-1ff4-41e7-ae52-75a893253b37)

## Qdrant vector storage- 
![image](https://github.com/Adii2202/Athina-AI/assets/131331573/e098923c-8de2-47ac-855e-2dde45436f92)

