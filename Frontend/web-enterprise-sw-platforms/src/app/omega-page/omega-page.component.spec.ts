import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OmegaPageComponent } from './omega-page.component';

describe('OmegaPageComponent', () => {
  let component: OmegaPageComponent;
  let fixture: ComponentFixture<OmegaPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OmegaPageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OmegaPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
