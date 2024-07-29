from tkinter import *
from tkinter import messagebox

import matplotlib.pyplot as plt

from src.BST import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('Árvore Binária de Busca')
        self.geometry('{}x{}'.format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.wm_state('zoomed')
        self.bst = BST()
        
        self.canvas = Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight() / 0.01, bg="slategrey", relief=RAISED, bd=12)
        self.canvas.place(x=0, y=160)
        
        self.canvas.bind('<MouseWheel>', self.zoom)
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.dragging)
                        
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Nome").pack()
        self.name_entry = Entry(self)
        self.name_entry.pack()

        Button(self, text="Inserir", command=self.insert_name).place(x=570, y=20)
        self.bind('<Return>', lambda e: self.insert_name())
        Button(self, text="Apagar", command=self.delete_name).place(x=750, y=20)
        Button(self, text="Carregar entrada.txt", command=self.abrir_entrada).place(x=500, y=50)
        Button(self, text="Exportar", command=self.exportar_entrada).place(x=750, y=50)
        Button(self, text="Mostrar informações", command=self.show_info).pack()
        Button(self, text="Mostrar travessias", command=self.show_traversals).pack()
        Button(self, text="Resetar Zoom", command=self.reset_zoom).pack()
        
    def abrir_entrada(self):
        try:
            with open('entrada.txt', 'r') as file:
                data = file.read().strip().split(',')
            for name in data:
                if name:
                    if self.bst.exists(self.bst.root, name):
                        pass
                        #messagebox.showerror("Erro", f"'{name}' já existe na BST")
                    else:
                        self.bst.insert(name)
            self.reset_zoom()
            # messagebox.showinfo("Sucesso! ", "Dados carregados com sucesso")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo 'entrada.txt' não encontrado")
                
    def exportar_entrada(self):
        try:
            # Obtém os nomes da BST usando level_order
            data = self.bst.levelOrderTraversal()
            data = ','.join(data)
            
            # Escreve os dados no arquivo 'entrada.txt'
            with open('entrada.txt', 'w') as file:
                file.write(data)
            
            # Optionally, show a success message
            messagebox.showinfo("Sucesso! ", "Dados exportados com sucesso")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar dados: {str(e)}")
            
    def zoom(self, event):
        scale = 1.0
        if event.delta > 0 or event.num == 4:
            scale = 1.1
        elif event.delta < 0 or event.num == 5:
            scale = 0.9
        self.canvas.scale("all", event.x, event.y, scale, scale)
        
    def start_drag(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def dragging(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    
    def insert_name(self):
        name = self.name_entry.get()
        if name:
            if self.bst.exists(self.bst.root, name):
                messagebox.showerror("Erro", f"'{name}' já existe na BST")
            else:
                self.bst.insert(name)
                self.reset_zoom()
                # messagebox.showinfo("Sucesso! ", f"'{name}' foi inserido na BST")
            self.name_entry.delete(0, 'end')
            
    def delete_name(self):
        name = self.name_entry.get()
        if name == '':
                name = self.bst.maxValueNode(self.bst.root)
        if self.bst.exists(self.bst.root, name) == False:
            messagebox.showerror("Erro", f"'{name}' não existe na BST")
        else:
            if self.bst.remove(name):
                self.reset_zoom()
                # messagebox.showinfo("Sucesso! ", f"'{name}' foi removido da BST")
        self.name_entry.delete(0, 'end')
    
    def show_info(self):
        size = self.bst.size(self.bst.root)
        height = self.bst.height(self.bst.root)
        if self.bst.root:
            min_val = self.bst.minValueNode(self.bst.root)
            max_val = self.bst.maxValueNode(self.bst.root)
        else:
            min_val = max_val = "A árvore está vazia"
        leaves = self.bst.leafNodes(self.bst.root, [])
        internal_path_length = self.bst.internalPathLength(self.bst.root)
        is_balanced = self.bst.isBalanced(self.bst.root)
        info = f"Tamanho: {size}\nAltura: {height}\nValor Mínimo: {min_val}\nValor Máximo: {max_val}\nNós folhas: {leaves}\n\nComprimento Interno: {internal_path_length}\n\nEstá balanceada? {is_balanced}"
        messagebox.showinfo("Informação da Árvore", info)

    def show_traversals(self):
        inorder = self.bst.inorderTraversal(self.bst.root, [])
        postorder = self.bst.postorderTraversal(self.bst.root, [])
        preorder = self.bst.preorderTraversal(self.bst.root, [])
        levelorder = self.bst.levelOrderTraversal()
        traversals = f"Pré ordem: {', '.join(preorder)}\nEm ordem: {', '.join(inorder)}\nPós ordem: {', '.join(postorder)}\nLevel order: {', '.join(levelorder)}"
        messagebox.showinfo("Travessias na Árvore", traversals)
    
    def reset_zoom(self):
        # Limpa o canvas
        self.canvas.delete("all")
        # Redefine a posição de rolagem do canvas para a posição inicial
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)
        # Redesenha a árvore a partir da raiz
        self.draw_tree(self.bst.root)
        
    def draw_tree(self, node, x = 680, y = 30, layer = -1, pos = {}):
        if node is not None:
            # Calcular a largura do nó com base no tamanho do nome
            node_width = max(50, len(node.val) * 10)
            node_height = 30  # Altura fixa

            # Calcular a posição do nó
            if node not in pos:
                pos[node] = (x, y)

            # Obter a altura total da árvore
            total_height = self.bst.height(self.bst.root)

            # Ajustar espaçamento horizontal e vertical
            horizontal_spacing = 8 * (2 ** (total_height - layer))
            vertical_spacing = 50

            # Desenhar as arestas e calcular as posições dos filhos
            if node.left:
                left_x = x - horizontal_spacing
                left_y = y + vertical_spacing
                self.canvas.create_line(x, y, left_x, left_y)
                self.draw_tree(node.left, left_x, left_y, layer + 1, pos)
            if node.right:
                right_x = x + horizontal_spacing
                right_y = y + vertical_spacing
                self.canvas.create_line(x, y, right_x, right_y)
                self.draw_tree(node.right, right_x, right_y, layer + 1, pos)
                
            # Desenhar o nó
            self.canvas.create_oval(x - node_width / 2, y - node_height / 2, x + node_width / 2, y + node_height / 2, fill="green", outline="blue")
            self.canvas.create_text(x, y, text=node.val)

if __name__ == "__main__":
    app = App()
    app.mainloop()