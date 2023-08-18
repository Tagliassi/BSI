public class ControleRemoto implements Controlador{
    private int volume;
    private boolean ligado;
    private boolean tocando;

    public ControleRemoto(){
        this.volume = 50;
        this.ligado = false;
        this.tocando = false;
    }

    private int getVolume() {
        return volume;
    }

    private boolean isLigado() {
        return ligado;
    }

    private boolean isTocando() {
        return tocando;
    }

    private void setLigado(boolean ligado) {
        this.ligado = ligado;
    }

    private void setTocando(boolean tocando) {
        this.tocando = tocando;
    }

   private void setVolume(int volume) {
       this.volume = volume;
   }

@Override
public void ligar() {
    this.setLigado(true);
}

@Override
public void desligar() {
    this.setLigado(false);
}

@Override
public void abrirMenu() {
    System.out.println("Está ligado: " + this.isLigado());
    System.out.println("Está tocando: "+ this.isTocando());
    System.out.print("Volume: "+ this.getVolume());
    for (int i = 0; i <= this.getVolume(); i+=10) {
        System.out.print("|");
    }

}

@Override
public void fecharMenu() {
    System.out.println("Fechando menu...");
}

@Override
public void maisVolume() {
    if(this.isLigado()){
        this.setVolume(this.getVolume()+1);
    }
}

@Override
public void menosVolume() {
    if(this.isLigado()){
        this.setVolume(this.getVolume()-1);
    }
}

@Override
public void ligarMudo() {
    if(this.isLigado() && this.getVolume()>0){
        this.setVolume(0);
    }
}

@Override
public void desligarMudo() {
    if(this.isLigado() && this.getVolume()==0){
        this.setVolume(50);
    }
}

@Override
public void play() {
    if(this.isLigado() && !(isTocando())){
        this.setTocando(true);
    }
}

@Override
public void pause() {
    if(this.isLigado() && isTocando()){
        this.setTocando(false);
    }
}
}
