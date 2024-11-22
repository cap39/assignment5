package JavaFiles;
// CityServiceManager.java
import java.util.HashMap;
import java.util.Map;

public class CityServiceManager {
    private Map<String, RideServiceGo> services = new HashMap<>();

    public void addService(String serviceName, RideServiceGo servicePrototype) {
        services.put(serviceName, servicePrototype);
    }

    public RideServiceGo getService(String serviceName) {
        RideServiceGo service = services.get(serviceName);
        return service != null ? service.cloneService() : null;
    }
}