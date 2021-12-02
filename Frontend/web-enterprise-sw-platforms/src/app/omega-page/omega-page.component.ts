import { Component, OnInit } from '@angular/core';
import { AppServiceService } from '../app-service.service'
import { AppComponent } from '../app.component';
@Component({
  selector: 'app-omega-page',
  templateUrl: './omega-page.component.html',
  styleUrls: ['./omega-page.component.css']
})
export class OmegaPageComponent implements OnInit {
  notification: any;
  notifcationSuccess = false;
  constructor(private service:AppServiceService, private appComponent: AppComponent) { }

  ngOnInit(): void {
  }
  sendNotifications () {
    this.service.postNotifications(this.notification)
    .subscribe(response => {
      this.appComponent.getData()
      this.notification = ''
      this.notifcationSuccess = true
    })
  }
}
