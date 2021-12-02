import { Injectable } from '@angular/core';
import { Router,NavigationStart, Event as NavigationEvent } from '@angular/router';
import { Location } from '@angular/common';
@Injectable({
  providedIn: 'root'
})
export class AuthService {
 
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
