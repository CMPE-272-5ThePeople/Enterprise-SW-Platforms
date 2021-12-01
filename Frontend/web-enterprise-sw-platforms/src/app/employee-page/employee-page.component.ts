import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-employee-page',
  templateUrl: './employee-page.component.html',
  styleUrls: ['./employee-page.component.css']
})
export class EmployeePageComponent implements OnInit {
  
  constructor() { }

  ngOnInit(): void {
  }
  openProjectVal: boolean=true;
  openTrainingsVal: boolean=false;
  training: String='';
  openProjects () {
    this.openProjectVal = true
    this.openTrainingsVal = false
  }
  openTrainings () {
    this.openTrainingsVal = true
    this.openProjectVal = false
  }
  trainingValue (training:any) {
    console.log(training)
  }
}
