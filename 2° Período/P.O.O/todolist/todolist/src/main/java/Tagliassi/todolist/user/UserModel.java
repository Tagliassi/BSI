package Tagliassi.todolist.user;

import java.util.UUID;

import jakarta.persistence.Entity;
import lombok.Data;

@Data
@Entity(name="tb_users")
public class UserModel {

    private UUID id;

    private String username;
    private String name;
    private String password;
   
}
