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
  public sendGetRequest(): Observable<Post[]>{
    return this.httpClient.get<Post[]>(this.url);
  }

  public getNotifications(): Observable<Notifications[]> {
    let returnVal = this.httpClient.get<Notifications[]>('https://omega-django-backend.herokuapp.com/api/get_all_notifications/')
    return returnVal
  }

  public postNotifications(message:any) {
    const formData = new FormData();
    formData.append('message', message);
    return this.httpClient.post('https://omega-django-backend.herokuapp.com/api/get_all_notifications/', formData)
  }
}
