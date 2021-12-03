import { Component, OnInit } from '@angular/core';
import { AppServiceService } from '../app-service.service'; 
import * as _ from 'lodash'
@Component({
  selector: 'app-manager-page',
  templateUrl: './manager-page.component.html',
  styleUrls: ['./manager-page.component.css']
})

export class ManagerPageComponent implements OnInit {
  employees:any;
  finalemployees:any=['Swathi','Shreya','Aryan'];
  selectedemp:any;
  numberOfDepartment:any;
  numberOfEmployees:any;
  keysValues:any;
  employeeIDs:any;
  constructor(private service:AppServiceService) { }
  
  ngOnInit(): void {
    this.service.getEmployees().subscribe(response=>{
      this.employees = Object.values(response)
      this.finalemployees = Object.values(this.employees[1])
      let group = _.groupBy(this.finalemployees, 'department_name');
      this.numberOfDepartment = Object.keys(group).length
      this.numberOfEmployees = this.finalemployees.length
      this.keysValues = Object.keys(group).toString()
      this.employeeIDs = _.filter(this.finalemployees, 'employeeid')
      console.log(this.keysValues)
    })
  }
  onSubmit() {
  }
 
}
