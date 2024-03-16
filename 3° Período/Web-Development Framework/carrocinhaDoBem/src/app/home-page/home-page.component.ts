import { Component, OnInit } from '@angular/core';
import { PetsServiceService } from '../services/pets-service.service';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styles: ``
})

export class HomePageComponent implements OnInit {

  constructor(public service: PetsServiceService){

  }

  ngOnInit(): void {
    //this.service.getPets();
    throw new Error('Method not implemented.');
  }

}
