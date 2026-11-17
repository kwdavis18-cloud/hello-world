from pathlib import Path
import unittest


class SiteTests(unittest.TestCase):
    def test_hello_world_heading(self):
        html = Path("dist/index.html").read_text(encoding="utf-8")
        self.assertIn("<h1>hello, world!</h1>", html)

    def test_only_public_files_are_packaged(self):
        """Keep unexpected files, such as .env or source files, off the site."""
        root = Path("dist")
        files = {
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(files, {"index.html"})
        self.assertFalse(any(path.is_symlink() for path in root.rglob("*")))


if __name__ == "__main__":
    unittest.main()
