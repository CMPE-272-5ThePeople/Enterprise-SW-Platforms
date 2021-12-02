import { Component, OnInit } from '@angular/core';
import { AppServiceService } from '../app-service.service'
@Component({
  selector: 'app-manager-page',
  templateUrl: './manager-page.component.html',
  styleUrls: ['./manager-page.component.css']
})

export class ManagerPageComponent implements OnInit {
  employees:any;
  finalemployees:any=['Swathi','Shreya','Aryan'];
  selectedemp:any;
  constructor(private service:AppServiceService) { }
  
  ngOnInit(): void {
    this.service.getEmployees().subscribe(response=>{
      this.employees = Object.values(response)
      this.finalemployees = Object.values(this.employees[1])
    })
  }
  onSubmit() {
  }
 
}
