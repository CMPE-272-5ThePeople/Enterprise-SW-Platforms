import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'web-enterprise-sw-platforms';
  constructor (private router: Router) {}
  checkRoute () {
    return this.router.url === '/emp'
  }
}
