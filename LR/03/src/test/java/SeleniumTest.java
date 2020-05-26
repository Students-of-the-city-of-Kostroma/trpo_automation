
import org.junit.After;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;


import java.util.Arrays;
import java.util.Collection;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

@RunWith(value = Parameterized.class)
public class SeleniumTest {

    private String url;
    private String number;
    private Selenium selen;
    private String expected;
    private String expectedrez;

    // Inject via constructor
    // for {8, 2, 10}, numberA = 8, numberB = 2, expected = 10
    public SeleniumTest(String url, String  number,String expected,String expectedrez ) {
        this.url=url;
        this.number=number;
        this.expected=expected;
        this.expectedrez=expectedrez;
        selen=new Selenium(url,number);

    }

    // name attribute is optional, provide an unique name for test
    // multiple parameters, uses Collection<Object[]>
    @Parameters(name = "{index}: testid_{1}_{2}")
    public static Collection<Object[]> data() {
        return Arrays.asList(new Object[][]{

                {"https://github.com/vvtatyana/Pin","6","0","Имя milestone некорректно\n"},

        });
    }

    @Test
    public void test() {
        selen.test();
        assertThat(selen.Get_Ozenka(), is(expected));
        assertThat(selen.Get_Result(), is(expectedrez));
        System.out.println(selen.Get_Result());
    }



}