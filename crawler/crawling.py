import os
import argparse
import base64
from enum import Enum
from six.moves.urllib.parse import urlparse

from icrawler import ImageDownloader
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import GoogleImageCrawler


class SearchEngine(Enum):
    BING = "bing"
    GOOGLE = "google"


def setting_args():
    """Parse command line arguments for the image crawler.

    Returns:
        Namespace: Containing parsed arguments.
    """
    parser = argparse.ArgumentParser(description="crawling images")
    parser.add_argument("-o", "--output", default="./images", type=str)
    parser.add_argument("-n", "--N", default=10, type=int)
    parser.add_argument("-e", "--engine", default="google", type=str)
    return parser.parse_args()


class Base64NameDownloader(ImageDownloader):
    def get_filename(self, task, default_ext):
        """Base64 encodes the URL path and generates a file name.

        Args:
            task (dict): A dictionary with a "file_url" key.
            default_ext (str): A default extension to use.

        Returns:
            str: The generated filename.
        """
        url_path = urlparse(task["file_url"])[2]
        # If the image contains an extension, get it.
        if "." in url_path:
            extension = url_path.split(".")[-1]
            if extension.lower() not in [
                "jpg",
                "jpeg",
                "png",
            ]:
                extension = default_ext
        else:
            extension = default_ext
        # Encoding the URL to the file name.
        filename = base64.b64encode(url_path.encode()).decode()
        return f"{filename}.{extension}"


def get_crawler(args, dir_name):
    """Returns a crawler object based on the search engine in the arguments.

    Args:
        args (argparse.Namespace): Containing parsed arguments.
        dir_name (str): The output directory for downloaded images.

    Returns:
        A crawler object for the selected search engine.
    """
    if args.engine == SearchEngine.BING.value:
        crawler = BingImageCrawler(
            downloader_cls=Base64NameDownloader, storage={"root_dir": dir_name}
        )
    elif args.engine == SearchEngine.GOOGLE.value:
        crawler = GoogleImageCrawler(storage={"root_dir": dir_name})
    return crawler


def main(args):
    """Main processing.

    Args:
        args (argparse.Namespace): Containing parsed arguments.
    """
    SEARCH_FILE = "./configs/search.txt"
    print("Start crawling images...")
    with open(SEARCH_FILE, encoding="utf_8") as f:
        read_data = list(f)
    # If there is no output directory, create it.
    os.makedirs(args.output, exist_ok=True)

    for i in range(len(read_data)):
        # Setting the directory name to save.
        dir_name = os.path.join(args.output, read_data[i].replace("\n", ""))

        crawler = get_crawler(args, dir_name)
        crawler.crawl(keyword=read_data[i], max_num=args.N)
    print("Finish crawling images!")


if __name__ == "__main__":
    args = setting_args()
    main(args)
