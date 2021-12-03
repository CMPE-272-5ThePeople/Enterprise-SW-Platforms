import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutPageComponent } from './about-page/about-page.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { AuthGuard } from './auth-guard';
import { SignUpComponent } from './auth/sign-up/sign-up.component';
import { EmployeePageComponent } from './employee-page/employee-page.component';
import { LoginPageComponent } from './login-page/login-page.component'
import { ManagerPageComponent } from './manager-page/manager-page.component';
import { NoAccessComponent } from './no-access/no-access.component';
import { OmegaPageComponent } from './omega-page/omega-page.component';

const routes: Routes = [
  { path: 'home', component: LoginPageComponent },
  { path: 'about', component: AboutPageComponent },
  { path: 'emp', component: EmployeePageComponent, canActivate: [AuthGuard] },
  { path: 'manager', component: ManagerPageComponent, canActivate: [AuthGuard] },
  { path: 'admin', component: AdminPageComponent },
  { path: 'omega', component: OmegaPageComponent, canActivate: [AuthGuard] },
  { path: 'noaccess', component: NoAccessComponent},
  {path: 'signup', component:SignUpComponent,canActivate: [AuthGuard]},
  { path: '**', redirectTo: 'home' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
