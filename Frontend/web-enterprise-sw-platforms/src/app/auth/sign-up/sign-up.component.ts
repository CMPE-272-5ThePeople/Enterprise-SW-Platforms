import { Component, OnInit } from '@angular/core';
import { CognitoUserPool,CognitoUserAttribute } from 'amazon-cognito-identity-js';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { environment } from 'src/environments/environment';
import { AppServiceService } from '../../app-service.service' 

interface formDataInterface {
  "name": string;
  "family_name": string;
  "email": string;
  "phone_number": string;
  [key: string]: string;
};

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html'
})
export class SignUpComponent implements OnInit {
  isLoading:boolean = false;
  fname:string = '';
  lname:string = '';
  email:string = '';
  mobileNo:string = '';
  password:string = '';
  alertValue:boolean=false;

  constructor(private router: Router, private service:AppServiceService) { }

  ngOnInit(): void {}

  onSignup(form: NgForm){
    if (form.valid) {
     this.isLoading = true;
     var poolData = {
      UserPoolId: "us-west-2_JaNWIhEZa",
      ClientId: "5qb4h3oijnu08htlsubpgo0m6b"
     };
     var userPool = new CognitoUserPool(poolData);
     var attributeList = [];
     let formData:formDataInterface = {
       "name": this.fname,
       "family_name": this.lname,
       "email": this.email,
       "phone_number": this.mobileNo
     }

     for (let key  in formData) {
       let attrData = {
         Name: key,
         Value: formData[key]
       }
       let attribute = new CognitoUserAttribute(attrData);
       attributeList.push(attribute)
     }
     userPool.signUp(this.email, this.password, attributeList, [], (
       err,
       result
     ) => {
       this.isLoading = false;
       if (err) {
         alert(err.message || JSON.stringify(err));
         return;
       }
       this.sendToBackend()
       this.alertValue = true
        this.fname = '';
        this.lname= '';
        this.email= '';
        this.mobileNo= '';
        this.password= '';
     });
    }
 }
 sendToBackend() {
  this.service.postToBackend(this.email,this.password).subscribe(response => {
    console.log(response)
  })
 }
}