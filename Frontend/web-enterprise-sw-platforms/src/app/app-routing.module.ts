import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutPageComponent } from './about-page/about-page.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { EmployeePageComponent } from './employee-page/employee-page.component';
import { LoginPageComponent } from './login-page/login-page.component'
import { ManagerPageComponent } from './manager-page/manager-page.component';
import { OmegaPageComponent } from './omega-page/omega-page.component';

const routes: Routes = [
  { path: 'login', component: LoginPageComponent },
  { path: 'about', component: AboutPageComponent },
  { path: 'emp', component: EmployeePageComponent },
  { path: 'manager', component: ManagerPageComponent },
  { path: 'admin', component: AdminPageComponent },
  { path: 'omega', component: OmegaPageComponent },
  { path: '**', component: LoginPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
