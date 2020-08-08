from unittest import TestLoader, TestSuite, TextTestRunner
from UnitTest_Login import AAF_Test1
from UnitTest_Logout import AAF_Test2
from UnitTest_ForgotPassword import AAF_Test3
from UnitTest_MaintanenceLogin import AAF_Test4
from UnitTest_MaintanenceRegister import AAF_Test5
from UnitTest_MaintanenceSearch import AAF_Test6
from UnitTest_EmployeeRegister import AAF_Test7
from UnitTest_CustomerDeleteBooking import AAF_Test8
from UnitTest_CustomerMakeBooking import AAF_Test9
from UnitTest_CustomerSearchPark import AAF_Test10
from UnitTest_CustomerViewBooking import AAF_Test11
from UnitTest_AddPark import AAF_Test12
from UnitTest_AddProperty import AAF_Test13
from UnitTest_EditPark import AAF_Test14
from UnitTest_UpdateProperty import AAF_Test15
from UnitTest_ViewBookings import AAF_Test16
from  UnitTest_AssignMaintanence import AAF_Test17
from UnitTest_AddCharges import AAF_Test18
from UnitTest_DeleteProperty import AAF_Test19
from UnitTest_DeletePark import AAF_Test20



if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(AAF_Test1),
        loader.loadTestsFromTestCase(AAF_Test2),
        loader.loadTestsFromTestCase(AAF_Test3),
        loader.loadTestsFromTestCase(AAF_Test4),
        loader.loadTestsFromTestCase(AAF_Test5),
        loader.loadTestsFromTestCase(AAF_Test12),
        loader.loadTestsFromTestCase(AAF_Test13),
        loader.loadTestsFromTestCase(AAF_Test6),
        loader.loadTestsFromTestCase(AAF_Test7),
        loader.loadTestsFromTestCase(AAF_Test9),
        loader.loadTestsFromTestCase(AAF_Test10),
        loader.loadTestsFromTestCase(AAF_Test11),
        loader.loadTestsFromTestCase(AAF_Test16),
        loader.loadTestsFromTestCase(AAF_Test17),
        loader.loadTestsFromTestCase(AAF_Test18),
        loader.loadTestsFromTestCase(AAF_Test14),
        loader.loadTestsFromTestCase(AAF_Test19),
        loader.loadTestsFromTestCase(AAF_Test20),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)