from textnode import TextNode, TextType


def main():
    tn1 = TextNode("This is a text node 1", TextType.BOLD_TEXT, "https://www.test.com")
    tn2 = TextNode(
        "This is a text node 2", TextType.ITALIC_TEXT, "https://www.test.com"
    )
    tn3 = TextNode("This is a text node 1", TextType.BOLD_TEXT, "https://www.test.com")
    print(tn1)
    print(tn2)
    print(tn3)

    print(f"tn1 vs tn2: {tn1 == tn2}")
    print(f"tn1 vs tn3: {tn1 == tn3}")


if __name__ == "__main__":

    main()
