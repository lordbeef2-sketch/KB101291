# OFFICIAL REPOSITORY FILE: SysML-v2-API-Services/test/controllers/HomeControllerTest.java

- repository: `SysML-v2-API-Services`
- source_path: `test/controllers/HomeControllerTest.java`
- source_url: https://github.com/Systems-Modeling/SysML-v2-API-Services/blob/0af711b14bbcea7b240bb0a3a65817ae68302092/test/controllers/HomeControllerTest.java
- source_bytes: 835
- source_sha256: `cc3043e650a871b13eb3a1b545d77bb4aa3066a5a33f924603bef56a25b68f93`
- decoded_as: `utf-8`


## EXACT SOURCE

````java
package controllers;

import org.junit.Test;
import play.Application;
import play.inject.guice.GuiceApplicationBuilder;
import play.mvc.Http;
import play.mvc.Result;
import play.test.WithApplication;

import static org.junit.Assert.assertEquals;
import static play.mvc.Http.Status.OK;
import static play.test.Helpers.GET;
import static play.test.Helpers.route;

public class HomeControllerTest extends WithApplication {

    @Override
    protected Application provideApplication() {
        return new GuiceApplicationBuilder().build();
    }

    @Test
    public void testIndex() {
        Http.RequestBuilder request = new Http.RequestBuilder()
                .method(GET)
                .uri("/");

        Result result = route(app, request);
        assertEquals(OK, result.status());
    }

}

````
