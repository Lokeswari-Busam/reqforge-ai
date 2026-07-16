from docx import Document

from app.AI.extractors.base_extractor import BaseExtractor


class DOCXExtractor(BaseExtractor):

    def extract_text(
        self,
        file_path: str,
    ) -> str:

        document = Document(file_path)

        return "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )