class Menu:
    def __init__(self, node):
        self.node = node

    def print_menu(self, indent=""):
        self._print_node_label(indent)
        children = self.node.children
        if not children:
            return
        self._print_children_labels(children)
        choice = self._get_choice(children)
        if choice == "b":
            return
        elif choice == "e":
            self._exit()
        selected_node = self._get_selected_node(children, choice)
        if not selected_node:
            print("Opcao invalida. tente com outra porfavor!.")
            self.print_menu()
        else:
            Menu(selected_node).print_menu()

    def _print_node_label(self, indent):
        print(f"\n{indent}({self.node.id}): {self.node.name}")

    def _print_children_labels(self, children):
        for child in children:
            if "[R]" in child.name:
                print(f"\n{child.name}\n")
            else:
                print(f"({child.id}): {child.name}")

    def _get_choice(self, children):
        return input("\nSelecione a seguiente opcao ou ('b' para voltar, 'E' pasa sair ): ")

    def _get_selected_node(self, children, choice):
        for child in children:
            if str(child.id) == choice:
                return child
        return None

    def _exit(self):
        print("saindo...")
        exit()
