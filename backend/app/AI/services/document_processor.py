import os

from app.AI.extractors import (
    PDFExtractor,
    DOCXExtractor,
    TXTExtractor,
)


class DocumentProcessor:

    def __init__(self):

        self.extractors = {
            ".pdf": PDFExtractor(),
            ".docx": DOCXExtractor(),
            ".txt": TXTExtractor(),
        }

    def extract_text(
        self,
        file_path: str,
    ) -> str:

        extension = os.path.splitext(
            file_path
        )[1].lower()

        extractor = self.extractors.get(
            extension,
        )

        if extractor is None:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

        return extractor.extract_text(
            file_path,
        )