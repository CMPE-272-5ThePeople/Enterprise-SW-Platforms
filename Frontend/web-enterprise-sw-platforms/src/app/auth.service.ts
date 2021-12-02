import { Injectable } from '@angular/core';
import { Router,NavigationStart, Event as NavigationEvent } from '@angular/router';
import { Location } from '@angular/common';
import { CognitoUserPool } from 'amazon-cognito-identity-js';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  isLoggedIn(): boolean {
    var isAuth = false;

    let poolData = {
      UserPoolId: "us-west-2_JaNWIhEZa",
      ClientId: "5qb4h3oijnu08htlsubpgo0m6b"
    };

    var userPool = new CognitoUserPool(poolData);
    var cognitoUser = userPool.getCurrentUser();

    if (cognitoUser != null) {
      cognitoUser.getSession((err: any, session: any) => {
        if (err) {
          alert(err.message || JSON.stringify(err));
        }
        isAuth = session.isValid();
      })
    }
    return isAuth;
  }
 
  returnValue: any
  constructor(private router: Router, location: Location) {
    
    
  }
  isAuthenticated(url: string) {
    let token = localStorage.getItem('role');
    token = '/'+token
    if (token === url) return true
    return false
  }
}
