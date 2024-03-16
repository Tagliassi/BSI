import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';


@Injectable({
  providedIn: 'root'
})
export class PetsServiceService {

  apiURL: string = environment.apiBaseUrl

  constructor(private http: HttpClient) { }

  /*
  getPets(): Observable<any> {
    return this.http.get<any>(`${this.apiURL}`)
    .subscribe({
      next: res=>{
        console.log(res)
      },
      error(err) {
          console.log(err)
      },
    });
  }

  insertPet(animal: IAnimal): Observable<any> {
    return this.http.post(`${apiUrl}`, animal);


  */
}
