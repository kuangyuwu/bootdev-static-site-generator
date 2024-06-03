from textnode import Textnode

def main() -> None:
    node = Textnode("This is a text node", "bold", "https://www.boot.dev")
    print(node)

if __name__ == '__main__':
    main()