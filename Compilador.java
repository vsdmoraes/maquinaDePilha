
import java.io.File;
import java.io.PrintStream;

class Compilador {

    public static void main(String[] args) {

        ArvoreSintatica arv = null;

        try {

            AnaliseLexica al = new AnaliseLexica("Entrada.txt");
            Parser as = new Parser(al);

            arv = as.parseProg();

            CodeGen backend = new CodeGen();

            String codigo = backend.geraCodigo(arv);

            PrintStream ps = new PrintStream(new File("Saida.txt"));
            ps.print(codigo);

            ps.close();

        } catch (Exception e) {
            System.out.println("Erro de compilação:\n" + e);
        }

    }
}
