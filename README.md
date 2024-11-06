# Document-Summarization-System

# Document Summarization System

This is a Python-based document summarization system that uses the TextRank algorithm to generate concise summaries of text documents.

## Features

- Reads and extracts text from input files
- Calculates sentence similarity using cosine distance
- Builds a similarity matrix and sentence similarity graph
- Ranks sentences using PageRank algorithm
- Selects the top-ranked sentences to create the summary
- Outputs a summary of the input text

## Key Steps

1. **Read Article**: The `read_article` function reads the content of a text file and returns it as a string.

2. **Calculate Sentence Similarity**: The `sentence_similarity` function calculates the cosine similarity between two sentences, ignoring any stopwords.

3. **Build Similarity Matrix**: The `build_similarity_matrix` function creates a similarity matrix for the given sentences, using the `sentence_similarity` function.

4. **Generate Summary**:
   - The `generate_summary` function reads the article from the given file
   - Splits the article into sentences
   - Generates the similarity matrix using `build_similarity_matrix`
   - Constructs a similarity graph using NetworkX
   - Ranks the sentences using PageRank algorithm
   - Selects the top `top_n` sentences to create the summary
   - Returns the summary as a string

## Prerequisites

- Python 3.x
- NLTK (Natural Language Toolkit)
- NumPy
- NetworkX

You can install the required dependencies using pip:

```
pip install nltk numpy networkx
```

## Usage

1. Import the `generate_summary` function from the `document_summarization` module:

   ```python
   from document_summarization import generate_summary
   ```

2. Call the `generate_summary` function with the path to the text file you want to summarize:

   ```python
   summary = generate_summary('path/to/your/document.txt')
   print(summary)
   ```

   The function will return a string containing the summary of the input text.

3. Optionally, you can specify the number of top sentences to include in the summary by passing the `top_n` parameter:

   ```python
   summary = generate_summary('path/to/your/document.txt', top_n=3)
   print(summary)
   ```

   This will generate a summary using the 3 top-ranked sentences.

## Example

Here's an example of how to use the document summarization system:

```python
from document_summarization import generate_summary

summary = generate_summary('path/to/your/document.txt')
print(summary)
```

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/document-summarization).

## License

This project is licensed under the [MIT License](LICENSE).
