import unittest
from Homework4a import repository_list


class TestRepositoryList(unittest.TestCase):
    def test_correct_response(self):
        correct_response = [
            ("AlamofirePractise", 16),
            ("algorithm", 2),
            ("ArthurChi.github.io", 7),
            ("Aspects", 30),
            ("audio_video_streaming", 30),
            ("awesome-ios-animation", 30),
            ("CFRuntime", 18),
            ("CJWebView", 3),
            ("CLion", 4),
            ("CoreTextpractise", 14),
            ("CS-Books", 27),
            ("DataStruct", 17),
            ("DemoCamera", 11),
            ("Download", 22),
            ("FileKit", 30),
            ("FM", 13),
            ("ImageLoadPractice", 1),
            ("iOS-WebView-JavaScript", 8),
            ("iOSDownload", 4),
            ("JSBridge", 16),
            ("JSCorePractise", 5),
            ("JSMutiPlatform", 9),
            ("LayerPractise", 6),
            ("LCCode", 26),
            ("LearnOpenGLES", 30),
            ("learn_os", 4),
            ("LSUnusedResources", 9),
            ("MediaEditor", 8),
            ("MetalDemo", 2),
            ("MySampleCode", 30),
        ]
        self.assertEqual(repository_list("ArthurChi"), correct_response)

    def test_nonexistent_user(self):
        "FAKE GITHUB ACCOUNT TEST"
        user_id = "NOTAREALUSERDONOTHAVEAGITHUBACCOUNTLMAO"
        self.assertEqual(
            repository_list(user_id),
            "ERROR: Cannot Retrieve Repository Data 404: Not Found",
        )

    def test_no_commits(self):
        """TEST USER WITH NO COMMITS"""
        self.assertEqual(
            repository_list("douglas0520"),
            "ERROR: Cannot Retrieve Commit Data 'F2023_SSW567' STATUS CODE: 200: OK",
        )


if __name__ == "__main__":
    unittest.main()
