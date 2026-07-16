from app.AI.services.document_processor import DocumentProcessor
from app.AI.processors.text_cleaner import TextCleaner
from app.AI.processors.text_chunker import TextChunker

processor = DocumentProcessor()
cleaner = TextCleaner()
chunker = TextChunker()

text = processor.extract_text(
    "uploads/requirements_employee_onboarding_2026-07-07_12-17-01.pdf"
)

clean_text = cleaner.clean(text)

chunks = chunker.chunk_text(clean_text)

print(f"Total Chunks: {len(chunks)}")

for index, chunk in enumerate(chunks, start=1):
    print(f"\n===== Chunk {index} =====\n")
    print(chunk)