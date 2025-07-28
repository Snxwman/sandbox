import random
import string


class Codec:
    base_url: str = 'https://tinyurl.com'
    slug_len: int = 6
    url_map: dict[str, str] = {}

    def generate_slug(self) -> str:
        """Generates a potential short url slug"""
        alphabet = string.ascii_letters + string.digits
        return ''.join(random.choices(alphabet, k=Codec.slug_len))

    def encode(self, long_url: str) -> str:
        """Encodes a URL to a shortened URL."""
        while (short_url := f'{Codec.base_url}/{self.generate_slug()}') in self.url_map:
            continue

        self.url_map[short_url] = long_url
        return short_url

    def decode(self, short_url: str) -> str:
        """Decodes a shortened URL to its original URL."""
        if short_url in self.url_map:
            return self.url_map[short_url]
        return ''
