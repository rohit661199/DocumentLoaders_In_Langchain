from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs = loader.load()
print(len(docs))
print(docs[11].page_content)
print(docs[11].metadata)


#docs = loader.lazy_load()
#for document in docs:
#print(document.metadata)