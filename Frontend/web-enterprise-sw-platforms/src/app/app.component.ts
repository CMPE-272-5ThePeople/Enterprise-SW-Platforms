import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AppServiceService } from '../app/app-service.service'
import Notifications from './models/notifications'
import { NavigationStart, Event as NavigationEvent } from '@angular/router';
import * as _ from 'lodash';
import { CognitoUserPool } from 'amazon-cognito-identity-js';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'web-enterprise-sw-platforms';
  notifications: any;
  finalnotifications = Array<any>();
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
  getData() {
    this.service.getNotifications().subscribe(response => {
      this.notifications = Object.values(response)
      this.finalnotifications = Object.values(this.notifications[1])
    })
  }
  onLogout() {
    let poolData = {
      UserPoolId: "us-west-2_JaNWIhEZa",
      ClientId: "5qb4h3oijnu08htlsubpgo0m6b"
    };
    let userPool = new CognitoUserPool(poolData);
    let cognitoUser = userPool.getCurrentUser();
    cognitoUser?.signOut();
    this.loginValue = false
    localStorage.removeItem('role')
    localStorage.clear()
    this.router.navigate(["home"])
  }
  ngOnInit() {
    this.getData()
  }
}
