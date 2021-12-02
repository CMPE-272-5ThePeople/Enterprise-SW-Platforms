import { Injectable } from '@angular/core';
import { Router, CanActivate, RouterStateSnapshot, ActivatedRouteSnapshot } from '@angular/router';
import { AuthService } from './auth.service'
@Injectable()
export class AuthGuard implements CanActivate {

    constructor(private router: Router
        , private authService: AuthService) {}

    canActivate(next: ActivatedRouteSnapshot,
        state: RouterStateSnapshot) {
        // Check to see if a user has a valid token
        let url: string = state.url;
        return this.checkLogin(url);
        
        
    }
    checkLogin (url: string) {
        console.log(url)
        if (this.authService.isAuthenticated(url)) {
            return true;
        }   else {
            this.router.navigate(['/noaccess']);
            return false;
        }
    }

}