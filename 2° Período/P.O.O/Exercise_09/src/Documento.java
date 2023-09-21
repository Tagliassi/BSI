public abstract class Documento extends Arquivo {
    
}

class Texto extends Documento{

    public void mostrar(){
        System.out.println("Mostrando Texto");
    }    

}

class Imagem extends Documento{

    public void mostrar(){
        System.out.println("Mostrando Imagem");
    }    
}

class Video extends Documento{

    public void mostrar(){
        System.out.println("Mostrando Video");
    }    
    
}

class Som extends Documento{

    public void mostrar(){
        System.out.println("Mostrando Som");
    }    
    
}

class Planilha extends Documento{

    public void mostrar(){
        System.out.println("Mostrando Planilha");
    }    
    
}

class Apresentacao extends Documento{

    public void mostrar(){
        System.out.println("Mostrando Apresentação");
    }    
    
}