import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgForm } from '@angular/forms';
import { AuthenticationDetails, CognitoUser, CognitoUserPool } from 'amazon-cognito-identity-js';
import { environment } from 'src/environments/environment';
import jwt_decode from "jwt-decode";
@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {

  isLoading: boolean = false;
  email_address: string = "";
  password: string = "";

  constructor(private router: Router) { }

  ngOnInit(): void { }

  login(form: NgForm) {
    if (form.valid) {
      this.isLoading = true;
      let authenticationDetails = new AuthenticationDetails({
        Username: this.email_address,
        Password: this.password,
      });
      let poolData = {
        UserPoolId: environment.cognitoUserPoolId, // Your user pool id here
        ClientId: environment.cognitoAppClientId // Your client id here
      };

      let userPool = new CognitoUserPool(poolData);
      let userData = { Username: this.email_address, Pool: userPool };
      var cognitoUser = new CognitoUser(userData);
      cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: (result) => {
          console.log(result.getIdToken())

          var sessionIdInfo: any;
          sessionIdInfo = jwt_decode(result.getIdToken().getJwtToken());
          console.log(sessionIdInfo['cognito:groups']);
          if(sessionIdInfo['cognito:groups'][0] === 'employee') {
            localStorage.setItem('role', 'emp')
            this.router.navigate(["emp"])
          } else if(sessionIdInfo['cognito:groups'][0] === 'manager') {
            localStorage.setItem('role', 'manager')
            this.router.navigate(["manager"])
          } else if(sessionIdInfo['cognito:groups'][0] === 'omega') {
            localStorage.setItem('role', 'omega')
            this.router.navigate(["omega"])
          } else if(sessionIdInfo['cognito:groups'][0] === 'admin') {
            localStorage.setItem('role', 'admin')
            this.router.navigate(["signup"])
          }
        },
        onFailure: (err) => {
          alert(err.message || JSON.stringify(err));
          this.isLoading = false;
        },
      });
    }
  }
}
