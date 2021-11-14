# from google.cloud import language_v1

# def sample_analyze_sentiment(text_content):
#     """
#     Analyzing Sentiment in a String

#     Args:
#       text_content The text content to analyze
#     """

#     client = language_v1.LanguageServiceClient()

#     # text_content = 'I am so happy and joyful.'

#     # Available types: PLAIN_TEXT, HTML
#     type_ = language_v1.Document.Type.PLAIN_TEXT

#     # Optional. If not specified, the language is automatically detected.
#     # For list of supported languages:
#     # https://cloud.google.com/natural-language/docs/languages
#     language = "en"
#     document = {"content": text_content, "type_": type_, "language": language}

#     # Available values: NONE, UTF8, UTF16, UTF32
#     encoding_type = language_v1.EncodingType.UTF8

#     response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
#     # Get overall sentiment of the input document
#     print(u"Document sentiment score: {}".format(response.document_sentiment.score))
#     print(
#         u"Document sentiment magnitude: {}".format(
#             response.document_sentiment.magnitude
#         )
#     )
#     # Get sentiment for all sentences in the document
#     for sentence in response.sentences:
#         print(u"Sentence text: {}".format(sentence.text.content))
#         print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
#         print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))

#     # Get the language of the text, which will be the same as
#     # the language specified in the request or, if not specified,
#     # the automatically-detected language.
#     print(u"Language of the text: {}".format(response.language))

# f = open("mixed.txt", "r")
# x = f.read()
# # print(x)

# sample_analyze_sentiment(x)

import argparse
from typing import ContextManager

from google.cloud import language_v1

def return_result(annotations):
    # score = annotations.document_sentiment.score
    # magnitude = annotations.document_sentiment.magnitude

    result = []
    for index, sentence in enumerate(annotations.sentences):
        sentence_sentiment = sentence.sentiment.score
        print(
            "Sentence {} has a sentiment score of {}".format(index, sentence_sentiment)
        )
        result.append(sentence_sentiment)

    # print(
    #     "Overall Sentiment: score of {} with magnitude of {}".format(score, magnitude)
    # )
    return result




def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()
    content = movie_review_filename
    # with open(movie_review_filename, "r") as review_file:
    #     # Instantiates a plain text document.
    #     content = review_file.read()

    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    annotations = client.analyze_sentiment(request={"document": document})

    # Print the results
    return return_result(annotations)
    # print(annotations)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "movie_review_filename",
        help="The filename of the movie review you'd like to analyze.",
    )
    args = parser.parse_args()

    analyze(args.movie_review_filename)