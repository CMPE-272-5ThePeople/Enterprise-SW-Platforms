import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app/app-service.service'
import Notifications from './models/notifications'
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import * as _ from 'lodash';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'web-enterprise-sw-platforms';
  notifications: any;
  finalnotifications: any;
  loginValue: any;
  constructor(private router: Router, private service: AppServiceService) {
    let urlRoute = this.router.events.subscribe(
      (event: NavigationEvent) => {
        if (event instanceof NavigationStart) {
          if ('/home' === event.url || '/noaccess' === event.url) {
            this.loginValue = true
          }
        }
      })
  }
  getData () {
    this.service.getNotifications().subscribe(response => {
      this.notifications = Object.values(response)
      this.finalnotifications = Object.values(this.notifications[1])
    })
  }
  ngOnInit() {
    this.getData()

  }
}
