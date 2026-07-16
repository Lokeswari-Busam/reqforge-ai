class TextChunker:

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 1000,
        overlap: int = 150,
    ) -> list[str]:

        chunks = []

        start = 0

        while start < len(text):

            end = min(
                start + chunk_size,
                len(text),
            )

            if end < len(text):
                while end > start and text[end] != " ":
                    end -= 1

            chunks.append(
                text[start:end].strip()
            )

            start = end - overlap

            if start < 0:
                start = 0

        return chunks