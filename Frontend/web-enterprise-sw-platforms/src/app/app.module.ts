import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { EmployeePageComponent } from './employee-page/employee-page.component';
import { ManagerPageComponent } from './manager-page/manager-page.component';
import { AdminPageComponent } from './admin-page/admin-page.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { OmegaPageComponent } from './omega-page/omega-page.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NoAccessComponent } from './no-access/no-access.component';
import { AuthGuard } from './auth-guard';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    EmployeePageComponent,
    ManagerPageComponent,
    AdminPageComponent,
    AboutPageComponent,
    OmegaPageComponent,
    NoAccessComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [AuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
