import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Post } from './post';
import Notifications from './models/notifications';

@Injectable({
  providedIn: 'root'
})
export class AppServiceService {

  constructor(private httpClient: HttpClient) { }
  private url: string = 'https://jsonplaceholder.typicode.com/posts';
  public sendGetRequest(): Observable<Post[]> {
    return this.httpClient.get<Post[]>(this.url);
  }

  public getNotifications(): Observable<Notifications[]> {
    let returnVal = this.httpClient.get<Notifications[]>('https://backend-production-omega.herokuapp.com/api/get_notification_details/')
    return returnVal
  }

  public postNotifications(message: any) {
    const formData = new FormData();
    formData.append('message', message);
    return this.httpClient.post('https://backend-production-omega.herokuapp.com/api/get_notification_details/', formData)
  }


  public getEmployees() {
    return this.httpClient.get('https://backend-production-omega.herokuapp.com/api/get_employee_details/')
  }

  public postToBackend(email: any, password: any) {
    const formData1 = new FormData();
    formData1.append('username', email);
    formData1.append('email', email);
    formData1.append('password1', password);
    formData1.append('password2', password);
    return this.httpClient.post('https://backend-production-omega.herokuapp.com/api/create_user/', formData1)
  }
}
