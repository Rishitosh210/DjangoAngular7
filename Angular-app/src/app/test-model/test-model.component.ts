import { Component, OnInit } from '@angular/core';
import { TestModelService} from '../services/test-model.service';

@Component({
  selector: 'app-test-model',
  templateUrl: './test-model.component.html',
  styleUrls: ['./test-model.component.css']
})
export class TestModelComponent implements OnInit {
   	displayedColumns  :  string[] = ['id','test_char','test_int'];
	dataSource  = [];
  constructor(private contactService: TestModelService) { }

  ngOnInit() {
    this.fetchContacts();
  }

  fetchContacts(){
    this.contactService.getFirstPage().subscribe((data:  Array<object>) => {
      this.dataSource  =  data;
      console.log(this.dataSource);
    });
  }
}
