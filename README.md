 A end to end complete rag application 
 key insights:
  - uses gemini as an llm
  - uses llama-index as the framework
  - uses gemeini embedding to embed the document to vector

WORKFLOW

 - first the user uploads the document
 - it gets stored in out data folder 
 - whenever user make a query regarding the document first if there is no index present in our storage , a new index will be created
 - if it is present the previous index will be used
 - the index will convert the user query into embeddign
 - it will find the most similar embeeding to the user document
 - the the gemeini model will convert the the similar doucment accoring the user query and will reslu the result to the user
