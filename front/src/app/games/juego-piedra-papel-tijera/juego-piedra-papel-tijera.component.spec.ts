import { ComponentFixture, TestBed } from '@angular/core/testing';

import { JuegoPiedraPapelTijeraComponent } from './juego-piedra-papel-tijera.component';

describe('JuegoPiedraPapelTijeraComponent', () => {
  let component: JuegoPiedraPapelTijeraComponent;
  let fixture: ComponentFixture<JuegoPiedraPapelTijeraComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [JuegoPiedraPapelTijeraComponent]
    });
    fixture = TestBed.createComponent(JuegoPiedraPapelTijeraComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
