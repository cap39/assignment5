package JavaFiles;
public class CarBlackService extends RideService {
    public CarBlackService() {
        super(new CarBlackStrategy());
    }

    @Override
    public double calculateFare(double distance) {
        return pricingStrategy.calculateFare(distance);
    }
}