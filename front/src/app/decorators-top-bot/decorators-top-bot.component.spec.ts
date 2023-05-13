import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DecoratorsTopBotComponent } from './decorators-top-bot.component';

describe('DecoratorsTopBotComponent', () => {
  let component: DecoratorsTopBotComponent;
  let fixture: ComponentFixture<DecoratorsTopBotComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DecoratorsTopBotComponent]
    });
    fixture = TestBed.createComponent(DecoratorsTopBotComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
