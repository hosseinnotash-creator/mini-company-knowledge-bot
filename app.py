from pathlib import Path

DOCS_PATH = Path("docs")

documents = []

for file in DOCS_PATH.glob("*.md"):
    content = file.read_text(encoding="utf-8")
    documents.append(
        {
            "name": file.name,
            "content": content
        }
    )

question = input("Ask a question: ").lower()

for doc in documents:
    if any(word in doc["content"].lower() for word in question.split()):
        print("\nAnswer found in:", doc["name"])
        print(doc["content"])
        break
else:
    print("No relevant information found.")