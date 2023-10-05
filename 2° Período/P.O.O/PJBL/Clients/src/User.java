import java.util.Date;
import java.time.LocalDate;
import java.time.Period;
import java.time.ZoneId;

public abstract class User extends Contact {

    protected String name;
    protected Date birDate;
    protected Contact contactInfo;

    public User(String name, Date birDate, Contact contactInfo){
        this.name = name;
        this.birDate = birDate;
        this.contactInfo = contactInfo;
    }

    public int getAge() {
        Date birthDate = getBirDate(); 
        LocalDate today = LocalDate.now();
        LocalDate birthLocalDate = birthDate.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        Period period = Period.between(birthLocalDate, today);
        return period.getYears();
    }

    public String getName() {
        return name;
    }

    public Date getBirDate() {
        return birDate;
    }

   
}
