import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-register-pets',
  templateUrl: './register-pets.component.html',
  styles: ``
})

export class RegisterPetsComponent implements OnInit {

  constructor(){

  }

  ngOnInit(): void {
    //this.service.insertPet();
    throw new Error('Method not implemented.');
  }

}
